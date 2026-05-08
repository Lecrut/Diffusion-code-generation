import datetime
def manipulate_date(date_str, operation):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    if operation == 'increment':
        new_date = date_obj + datetime.timedelta(days=1)
    elif operation == 'decrement':
        new_date = date_obj - datetime.timedelta(days=1)
    else:
        return None
    return new_date
if __name__ == '__main__':
    initial_date_str = "2023-10-26"
    print(f"Initial Date: {initial_date_str}")
    incremented_date = manipulate_date(initial_date_str, 'increment')
    if incremented_date:
        print(f"Incremented Date: {incremented_date.strftime('%Y-%m-%d')}")
    decremented_date = manipulate_date(initial_date_str, 'decrement')
    if decremented_date:
        print(f"Decremented Date: {decremented_date.strftime('%Y-%m-%d')}")
    print("\n--- Further Examples ---")
    date_to_test = "2024-01-01"
    print(f"Testing with {date_to_test}")
    incremented_date_2 = manipulate_date(date_to_test, 'increment')
    if incremented_date_2:
        print(f"Incremented: {incremented_date_2.strftime('%Y-%m-%d')}")
    decremented_date_2 = manipulate_date(date_to_test, 'decrement')
    if decremented_date_2:
        print(f"Decremented: {decremented_date_2.strftime('%Y-%m-%d')}")