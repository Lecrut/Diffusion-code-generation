import random
def create_sample_list():
    data_types = ["string", "integer"]
    sample_list = []
    for i in range(10):
        item_type = random.choice(data_types)
        if item_type == "string":
            sample_list.append(f"Item {i+1} (String)")
        else:
            sample_list.append(i * 10)
    return sample_list
if __name__ == '__main__':
    my_list = create_sample_list()
    print("Dynamically Created List:")
    for index, item in enumerate(my_list):
        print(f"{index + 1}. {item}")