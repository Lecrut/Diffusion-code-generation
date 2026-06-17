class ListCounter:
    def count_occurrences(self, data_list, item):
        count = 0
        for element in data_list:
            if element == item:
                count += 1
        return count
if __name__ == '__main__':
    counter = ListCounter()
    sample_list = [1, 2, 3, 2, 4, 2, 5]
    item_to_find_present = 2
    item_to_find_absent = 99
    count1 = counter.count_occurrences(sample_list, item_to_find_present)
    print(f"Occurrences of {item_to_find_present} in {sample_list}: {count1}")
    count2 = counter.count_occurrences(sample_list, item_to_find_absent)
    print(f"Occurrences of {item_to_find_absent} in {sample_list}: {count2}")