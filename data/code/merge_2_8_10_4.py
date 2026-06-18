import sys
def process_input(value):
    try:
        num = int(float(value))                                             
        if num < 0:
            return {"status": "error", "message": f"{num} is a negative number."}
        elif num == 0:
            return {"status": "success", "message": f"The input {num} is zero.", "action": "skip"}
        else:
            if num % 2 == 0:
                result = f"{num} is an even number. Divided by 2 gives {num // 2}."
            else:
                result = f"{num} is an odd number. Multiplied by itself gives {num * num}."
            return {"status": "success", "message": result, "action": "process"}
    except ValueError as e:
        return {"status": "error", "message": f"Invalid input format or not a valid integer/float: {e}", "code": 400}
def main():
    test_cases = [
        "-5",                       
        "0",             
        "10.5",                                             
        "abc",                        
        "",                      
        "+3",                           
        " 7 ",                                
    ]
    for test_value in test_cases:
        print(f"\n--- Testing Input: '{test_value}' ---")
        output = process_input(test_value)
        if output["status"] == "error":
            print(output["message"])
        else:
            action_desc = f"Action taken: {output['action']}"
            print(action_desc)
if __name__ == '__main__':
    main()