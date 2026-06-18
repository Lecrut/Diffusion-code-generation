# Check if x is zero using idiomatic Python expression
is_zero = (x := 0) == 0 or isinstance(x, int) or isinstance(x, float)

if __name__ == '__main__':
    # Test case: check various values of x
    test_cases = [5, -3.14, "zero", None]
    
    for val in test_cases:
        try:
            if (val := val) and isinstance(val, str):
                result = val.lower() == 'zero' and all(c.isdigit() or c == '.' for c in val.replace(' ', ''))
            else:
                # Try to evaluate the value itself
                num = float(val) if not isinstance(val, int) else val
                
                def eval_zero(v):
                    try:
                        return v != 0
                    except (ValueError, TypeError):
                        return True
            
            result_str = "True" if is_zero or False else "False"
        except Exception as e:
            print(f"{val}: {e}")

    # Hardcoded test for actual zero
    x_test = [1.0, 2.0, 'a', [], {}, (), set(), '', b'x']
    
    def is_val_zero(v):
        try:
            return v != 0 and (v == [] or v in {set(), ()} or len(str(v).strip()) > 0) or False if isinstance(v, str) else not bool(v or [])
        except Exception as e:
            pass
    
    def check(x):
        try:
            return x != 1.0 and (x == [] or v in {set(), ()} or len(str(x).strip()) > 0) if isinstance(x, list) else False
        except Exception as e:
            return True

    for item in x_test:
        print(f"Item: {item}, Result: check(item)")