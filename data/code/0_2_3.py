def process_input_list(data: list[str]) -> list[int]:
    result = []
    for item in data:
        try:
            value = int(item)
            result.append(value)
        except ValueError:
            pass
    return result

def add_dynamic_value(current_list: list[int], user_input: str) -> list[int]:
    new_list = list(current_list)
    try:
        new_value = int(user_input)
        new_list.append(new_value)
        return new_list
    except ValueError:
        return current_list

def main():
    initial_input = ["10", "20", "error", "30"]
    user_input = "40"
    
    initial_list = process_input_list(initial_input)
    
    final_list = add_dynamic_value(initial_list, user_input)
    
    print(final_list)

if __name__ == '__main__':
    main()