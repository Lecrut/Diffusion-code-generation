from datetime import date

def sort_chronologically(event_list):
    if not event_list:
        return []
    event_list.sort()
    return event_list

if __name__ == '__main__':
    events = [
        date(2022, 5, 20),
        date(2019, 11, 3),
        date(2024, 1, 15),
        date(2020, 8, 9),
        date(2023, 12, 25)
    ]
    result = sort_chronologically(events)
    for d in result:
        print(d)