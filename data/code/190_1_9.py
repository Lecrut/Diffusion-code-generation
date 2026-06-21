TARGET_STRING = "example"

def check_target_presence(data_list):
    return TARGET_STRING in data_list

if __name__ == '__main__':
    sample_data = ["test", TARGET_STRING, "sample"]
    result1 = check_target_presence(sample_data)
    print(f"Does '{TARGET_STRING}' exist in the list? {result1}")

    empty_list = []
    result2 = check_target_presence(empty_list)
    print(f"Does '{TARGET_STRING}' exist in an empty list? {result2}")