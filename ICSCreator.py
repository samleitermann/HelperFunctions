from ics import Calendar, Event
import pytz
from datetime import datetime, timedelta

# Base date for the week (assuming the email date is accurate)
base_date = datetime(2024, 12, 9)  # Monday of the week

# Create a timezone object for 'America/New_York'
eastern_tz = pytz.timezone('America/New_York')

# Make the datetime object timezone-aware
base_date = eastern_tz.localize(base_date)

# Event details
events = [
    {"name": "Monday Practice", "start_time": "15:40", "end_time": "16:40", "date_offset": 0},
    {"name": "Tuesday Practice", "start_time": "18:40", "end_time": "19:40", "date_offset": 1},
    {"name": "Wednesday Practice", "start_time": "13:30", "end_time": "14:30", "date_offset": 2},
    {"name": "Thursday Practice", "start_time": "19:10", "end_time": "20:10", "date_offset": 3},
    {"name": "Friday Practice", "start_time": "18:40", "end_time": "19:40", "date_offset": 4},
    {"name": "First Match", "start_time": "11:00", "end_time": "12:00", "date_offset": 5},
]

# Create a new calendar
calendar = Calendar()

# Add events to the calendar
for event in events:
    event_date = base_date + timedelta(days=event["date_offset"])
    start = datetime.strptime(event["start_time"], "%H:%M").time()
    end = datetime.strptime(event["end_time"], "%H:%M").time()

    # Combine the date and time and localize to Eastern Time
    event_start = eastern_tz.localize(datetime.combine(event_date, start))
    event_end = eastern_tz.localize(datetime.combine(event_date, end))

    e = Event(name=event["name"], begin=event_start, end=event_end)
    calendar.events.add(e)

# Save the calendar to a file and overwrite old file(s).
file_path = "Squash_Week_Schedule.ics"
with open(file_path, "w") as f:
    f.writelines(calendar)

