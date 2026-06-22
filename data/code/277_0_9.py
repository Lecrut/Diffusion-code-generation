if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    
    def count_items(lst):
        count = 0
        for item in lst:
            count += 1
        return count
    
    num_items = count_items(sample_list)
    print(f"The number of items in the list is: {num_items}")