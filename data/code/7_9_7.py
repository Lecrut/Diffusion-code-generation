from datetime import datetime

UNIT_SECONDS = 1
UNIT_MINUTES = 60
UNIT_HOURS = 3600
UNIT_DAYS = 86400
UNIT_WEEKS = 604800

def compute_time_diff(dt_first, dt_second, target_unit):
    time_delta = dt_second - dt_first
    total_secs = abs(time_delta.total_seconds())
    if target_unit == "seconds":
        return total_secs
    if target_unit == "minutes":
        return total_secs / UNIT_MINUTES
    if target_unit == "hours":
        return total_secs / UNIT_HOURS
    if target_unit == "days":
        return total_secs / UNIT_DAYS
    if target_unit == "weeks":
        return total_secs / UNIT_WEEKS
    return total_secs

def format_structured_diff(dt_first, dt_second):
    time_delta = dt_second - dt_first
    total_secs = abs(time_delta.total_seconds())
    days_part = int(total_secs // UNIT_DAYS)
    rem_after_days = total_secs % UNIT_DAYS
    hours_part = int(rem_after_days // UNIT_HOURS)
    rem_after_hours = rem_after_days % UNIT_HOURS
    mins_part = int(rem_after_hours // UNIT_MINUTES)
    secs_part = int(rem_after_hours % UNIT_MINUTES)
    return {
        "days": days_part,
        "hours": hours_part,
        "minutes": mins_part,
        "seconds": secs_part
    }

if __name__ == '__main__':
    date_a = datetime(2023, 3, 15, 9, 30, 0)
    date_b = datetime(2023, 3, 17, 14, 45, 20)
    diff_in_hours = compute_time_diff(date_a, date_b, "hours")
    structured_breakdown = format_structured_diff(date_a, date_b)
    print(diff_in_hours)
    print(structured_breakdown)