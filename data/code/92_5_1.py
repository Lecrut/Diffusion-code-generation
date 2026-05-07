import sys
if __name__ == '__main__':
    input_data = "True\n"
    try:
        input_value = input_data.strip()
        if input_value.lower() == 'true':
            print('False')
        elif input_value.lower() == 'false':
            print('True')
        else:
            print("Invalid input")
    except Exception:
        pass