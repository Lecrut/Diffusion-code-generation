import random
def select_three_unique_names(name_list):
    if len(name_list) < 3:
        return []
    selected_names = random.sample(name_list, 3)
    return selected_names
if __name__ == '__main__':
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
    result = select_three_unique_names(names)
    print(result)