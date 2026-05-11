import random
def create_sample_list():
    data_types = ["string", "integer"]
    sample_list = []
    for _ in range(10):
        item_type = random.choice(data_types)
        if item_type == "string":
            sample_list.append(f"item_{random.randint(100, 999)}")
        else:
            sample_list.append(random.randint(1, 100))
    return sample_list
if __name__ == '__main__':
    my_list = create_sample_list()
    print("Dynamically created list of 10 sample items:")
    for index, item in enumerate(my_list):
        print(f"{index + 1}. {item}")