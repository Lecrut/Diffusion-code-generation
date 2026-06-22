def get_last_item(strings):
    if not strings:
        raise ValueError("The list is empty")
    return strings[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    last_item = get_last_item(sample_list)
    print(f"The last item in the list is: {last_item}")