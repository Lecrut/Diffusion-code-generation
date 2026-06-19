def get_last_item(lst):
    return lst[-1] if lst else None

if __name__ == '__main__':
    sample_data = "apple banana cherry"
    fruit_list = sample_data.split()
    last_fruit = get_last_item(fruit_list)
    print(last_fruit)