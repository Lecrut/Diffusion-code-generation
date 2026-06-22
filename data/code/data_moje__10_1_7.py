def get_first_element(lst):
    position_key = 'position_zero'
    position_map = {
        position_key: 0
    }
    index = position_map[position_key]
    return lst[index]

if __name__ == '__main__':
    inventory = ["hammer", "saw", "drill", "screwdriver"]
    first_item = get_first_element(inventory)
    print(first_item)