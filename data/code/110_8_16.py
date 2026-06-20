from datetime import date

events = [
    date(2023, 4, 15),
    date(2022, 9, 20),
    date(2023, 1, 1),
    date(2022, 12, 25)
]

def sort_events(event_list):
    event_list.sort()
    return event_list

if __name__ == '__main__':
    sorted_events = sort_events(events)
    for event in sorted_events:
        print(event)