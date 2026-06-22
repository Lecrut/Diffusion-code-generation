def retrieve_last_item(strings):
    if not strings:
        return None
    return strings[-1]

if __name__ == '__main__':
    SAMPLE_LIST = ["apple", "banana", "cherry", "date"]
    last_item = retrieve_last_item(SAMPLE_LIST)
    print(f"The last item in the list is: {last_item}")