import sys
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            radius = 5.0
        else:
            radius = float(input_data)
    except ValueError:
        radius = 0.0
    except Exception:
        radius = 0.0
    if radius > 0:
        area = 3.141592653589793 * (radius ** 2)
        print(area)
    else:
        print("Invalid radius provided.")