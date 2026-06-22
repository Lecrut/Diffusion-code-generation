import datetime

def resolve_weekday(date_component):
    calendar_reference = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    target_weekday_index = date_component.isoweekday()
    return calendar_reference[target_weekday_index]

def calculate_day_for_input(date_string):
    parsed_object = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    return resolve_weekday(parsed_object)

if __name__ == '__main__':
    sample_date_string = "2023-10-05"
    computed_day = calculate_day_for_input(sample_date_string)
    print(computed_day)