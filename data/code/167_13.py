def collect_and_store_data():
    data = {}
    sample_data = [
        ("Store A", 25),
        ("Store B", 30),
        ("Store C", 15),
        ("Store D", 42),
        ("Store E", 5)
    ]
    for store_name, age_str in sample_data:
        try:
            age = int(age_str)
            if age > 0:
                data[store_name] = age
            else:
                print(f"Error: Age for {store_name} must be positive.")
        except ValueError:
            print(f"Error: Invalid input for age for store {store_name}. Expected an integer.")
        except Exception as e:
            print(f"An unexpected error occurred for store {store_name}: {e}")
    return data
if __name__ == '__main__':
    final_data = collect_and_store_data()
    print(final_data)