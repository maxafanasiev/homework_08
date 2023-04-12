import datetime as DT

users = [
        {'name':'Bill', 'birthday':DT.datetime(1995,5,13)},
        {'name':'Jill', 'birthday':DT.datetime(1990,3,20)},
        {'name':'John', 'birthday':DT.datetime(1998,4,23)},
        {'name':'Jack', 'birthday':DT.datetime(1980,4,21)},
        {'name':'Ann', 'birthday':DT.datetime(1964,4,17)},
        {'name':'Helen', 'birthday':DT.datetime(1999,5,1)},
        {'name':'Max', 'birthday':DT.datetime(1991,5,3)},
        {'name':'Piter', 'birthday':DT.datetime(1984,4,16)},
        {'name':'Charles', 'birthday':DT.datetime(1989,4,16)},
        {'name':'Chack', 'birthday':DT.datetime(1993,4,15)}
          ]

WEEKDAYS = dict(Monday = [], 
                  Tuesday = [],
                  Wednesday = [],
                  Thursday = [],
                  Friday = [],
                  Saturday = [],
                  Sunday = [])

week_after = (DT.datetime.now() + DT.timedelta(days=7)).date()


def get_this_year_birthday(user):
    dt = user['birthday']
    new_dt = DT.datetime(DT.datetime.now().year,dt.month,dt.day)
    return new_dt


def get_weekday(user):
    return user['birthday'].strftime("%A")


def get_birthdays_per_week(users):
    for user in users:
        if get_this_year_birthday(user) > DT.datetime.now() and get_this_year_birthday(user).date() < week_after:
            if get_weekday(user) in ['Saturday', 'Sunday']:
                WEEKDAYS['Monday'].append(user['name'])
            else:
                WEEKDAYS[get_weekday(user)].append(user['name'])
    for day, value in WEEKDAYS.items():
        if len(value)>0:
            print('{:<15} : {:<100} '.format(day, ', '.join(value)))


if __name__ == '__main__':
    get_birthdays_per_week(users)




