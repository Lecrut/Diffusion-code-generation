import timeit
def create_name_set():
    return {"Alice", "Bob", "Charlie"}
if __name__ == '__main__':
    name_database = create_name_set()
    test_names = ["David", "Eve", "Frank"]
    start_time = timeit.default_timer()
    for name in test_names:
        if name in name_database:
            print(f"{name} exists")
        else:
            print(f"{name} does not exist")
    end_time = timeit.default_timer()
    elapsed_seconds = round(end_time - start_time, 4)
    print(f"Execution completed in {elapsed_seconds} seconds.")