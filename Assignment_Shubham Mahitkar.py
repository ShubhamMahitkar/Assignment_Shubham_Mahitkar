from pymongo import MongoClient

try:
    conn = MongoClient()
    print("Connected successfully!")
except:
    print("Could not connect to MongoDB")

db=conn.database

collection=db.useer

dictionary = { "_id, name", "phone", "address", "age", "sex"}

x = collection.insert_one(dictionary)









def binarySearch(number, SortedList):
      Low = 0
      High = len(SortedList) - 1
      while Low <= High :
            Mid = (High + Low) / 2
            if SortedList[Mid] == number:
                  return Mid
            elif SortedList[Mid] > number :
                  High=Mid - 1
            else :
                   Low = Mid + 1
      return "X";

def main():
      my_list = [_id]
      my_list = sorted(my_list)
      print my_list
      Sort = binarySearch(number, my_list)
      print Sort


if __name__ == "__main__":
      main()













def is_working_hours(public_holidays, week_holidays, work_timings):
    public_holidays1 = ['15 August', '26 January', '2 October']
    week_holidays1 = ["Saturday", "Sunday"]
    work_timings1 = [
      {"day": "Monday", "start": "9:30 am", "end": "6:30 pm"},
      {"day": "Tuesday", "start": "9:30 am", "end": "6:30 pm"},
      {"day": "Wednesday", "start": "9:30 am", "end": "6:30 pm"},
      {"day": "Thursday", "start": "9:30 am", "end": "6:30 pm"},
      {"day": "Friday", "start": "9:30 am", "end": "6:30 pm"},
      {"day": "Saturday", "start": "11:30 am", "end": "5:30 pm"}
    ]
    if public_holidays in public_holidays1:
        return False
    else:
        print("True")

    if week_holidays in week_holidays1:
        return True
    else:
        print("False")

    if work_timings >= 9.30 and work_timings <= 18.30:
        return False
    else:
        return True




public_holidays=input("enter ph: ")
week_holidays=input("enter wh: ")
print("Please Use 24 hour format")
work_timings = float(input("enter wt: "))

is_working_hours(public_holidays, week_holidays, work_timings)
