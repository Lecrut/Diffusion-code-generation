from collections import defaultdict

def get_or_create_defaultdict(data, composite_key, factory):
    if not isinstance(composite_key, tuple):
        composite_key = (composite_key,)
    
    if composite_key in data:
        return data[composite_key]
    
    data[composite_key] = factory()
    return data[composite_key]

if __name__ == '__main__':
    my_dict = defaultdict(list)
    key_tuple = ("user_1", "orders")
    
    def create_order_list():
        return ["initial_order"]
    
    result_new = get_or_create_defaultdict(my_dict, key_tuple, create_order_list)
    print(result_new)
    
    result_existing = get_or_create_defaultdict(my_dict, key_tuple, create_order_list)
    print(result_existing)
    
    result_new_key = get_or_create_defaultdict(my_dict, ("user_2", "orders"), create_order_list)
    print(result_new_key)