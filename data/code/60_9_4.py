if __name__ == '__main__':
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]
    if my_list:
        last_item = my_list[-1]
        print(f"The original list is: {my_list}")
        print(f"The last item in the list is: {last_item}")
    else:
        print("The list is empty.")