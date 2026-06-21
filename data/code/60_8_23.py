def get_last_item(strings):
    if not strings:
        return None
    return strings[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    last_item = get_last_item(sample_list)
    print(f"The last item in the list is: {last_item}")