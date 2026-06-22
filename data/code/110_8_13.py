from datetime import date

EVENT_CATEGORIES = {
    "conference": date(2023, 5, 15),
    "workshop": date(2022, 11, 20),
    "meetup": date(2024, 2, 10),
    "summit": date(2021, 8, 5),
    "gala": date(2023, 12, 1),
}

def sort_events_by_category(categories):
    event_list = list(categories.items())
    event_list.sort(key=lambda item: item[1])
    return event_list

if __name__ == '__main__':
    result = sort_events_by_category(EVENT_CATEGORIES)
    for category_name, event_date in result:
        print(f"{category_name}: {event_date}")