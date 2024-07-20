from fastapi import FastAPI , Query
from datetime import date
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(CORSMiddleware,
    allow_origins=["*"],  allow_methods=["*"],allow_headers=["*"],
)

class age(BaseModel):
    message : str
    age_in_yers : int
    age_in_months : int
    age_in_days : int
    age_in_h : int
   
@app.get("/")
def age_cal(day : int = Query (... , gt=0 , lt=32),
            month : int = Query (... , gt=0 , lt=13),
            year : int= Query (... , gt=0 , lt=2025)):
    today = date.today()
    dob = date(year,month,day)
    age_in_days = (today-dob).days
    age_in_yers = (today-dob).days / 365.24
    age_in_months = (today-dob).days / 30
    age_in_h = (today-dob).days*24
    
    age_in_yers = int(age_in_yers)
    age_in_months = int(age_in_months)
    age_in_h = int(age_in_h)
    
    if year < 1850:
        message = "اخبار فرعون؟"
    else :
        message = "العمر كله"
    
    return { "!النتيجة" : message ,
            "عمرك بالسنين" : age_in_yers ,
            "بالشهور" : age_in_months ,
            "بالايام" : age_in_days ,
            "بالساعات" : age_in_h}
    

