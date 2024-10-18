from datetime import date , time , datetime
# calling the today
# function of date class
today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nCurrent Dara and time is", now)

# Printing date's components
print("\nDate componets", today.year, today.month, today.day)