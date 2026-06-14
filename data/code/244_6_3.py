def calculate_area_sum(line1, line2):
    try:
        l1, w1 = map(float, line1.split())
        l2, w2 = map(float, line2.split())
        area1 = l1 * w1
        area2 = l2 * w2
        return area1 + area2
    except ValueError:
        return None
if __name__ == '__main__':
    input1 = "10 5"
    input2 = "4 6"
    result = calculate_area_sum(input1, input2)
    if result is not None:
        print(result)