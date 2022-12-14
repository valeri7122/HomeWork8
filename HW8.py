from datetime import datetime, timedelta


def get_birthdays_per_week(users):   
    
    dict = {'Monday:':'','Tuesday:':'','Wednesday:':'','Thursday:':'','Friday:':''}

    current_date = datetime.now()

    for user in users:
        congrate = current_date + timedelta(days=7)
        if  congrate.weekday == 6:
            congrate = current_date + timedelta(days=5)
        elif  congrate.weekday == 0:
            congrate = current_date + timedelta(days=6)  

        
        user_month = user['birthday'].month
        user_day = user['birthday'].day

        if congrate.weekday() == 1 and congrate.month == user_month and congrate.day == user_day:
            dict['Monday:'] += ' '+user['name']+','
        elif congrate.weekday() == 2 and congrate.month == user_month and congrate.day == user_day:
            dict['Tuesday:'] += ' '+user['name']+','
        elif congrate.weekday() == 3 and congrate.month == user_month and congrate.day == user_day:
            dict['Wednesday:'] += ' '+user['name']+','
        elif congrate.weekday() == 4 and congrate.month == user_month and congrate.day == user_day:
            dict['Thursday:'] += ' '+user['name']+','
        elif congrate.weekday() == 5 and congrate.month == user_month and congrate.day == user_day:
            dict['Friday:'] += ' '+user['name']+','                      

    for key, value in dict.items():
        print(key, value[:-1])


get_birthdays_per_week(users)

