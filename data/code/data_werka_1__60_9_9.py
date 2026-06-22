def get_last_item(lst):
    if not lst:
        raise ValueError("The list is empty.")
    return lst[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date", "elderberry"]
    try:
        last_element = get_last_item(sample_list)
        print(f"The list of strings is: {sample_list}")
        print(f"The last item in the list is: {last_element}")
    except ValueError as e:
        print(e)