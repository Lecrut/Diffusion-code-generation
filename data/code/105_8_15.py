from datetime import date

def find_next_weekday(target_index, reference):
    current_weekday = reference.weekday()
    offset = target_index - current_weekday
    if offset <= 0:
        offset += 7
    return reference.replace(day=reference.day + offset)

if __name__ == '__main__':
    start = date(2023, 9, 15)
    result = find_next_weekday(3, start)
    print(result)