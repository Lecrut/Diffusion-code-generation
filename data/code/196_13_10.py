def append_elements(source_list, target_list):
    target_list += source_list

if __name__ == '__main__':
    initial_list = [10, 20, 30]
    additional_values = [40, 50, 60]
    append_elements(initial_list, additional_values)
    print("Updated List:", initial_list)