import sys
if __name__ == '__main__':
    input_data = "True\n"
    try:
        input_value = input_data.strip()
        if input_value == "True":
            print("False")
        elif input_value == "False":
            print("True")
        else:
            print("Error: Invalid boolean input")
    except Exception:
        pass