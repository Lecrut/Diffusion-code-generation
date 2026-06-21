def concatenate_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    fruits = ["apple", "banana"]
    more_fruits = ["cherry", "date"]
    combined_fruits = concatenate_lists(fruits, more_fruits)
    print(combined_fruits)