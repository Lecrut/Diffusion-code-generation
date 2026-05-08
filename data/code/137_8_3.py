def assign_status(value, threshold):
    status = value > threshold
    return "Greater" if status else ("Less" if value < threshold else "Equal")
if __name__ == '__main__':
    x = 10
    t1 = 5
    t2 = 10
    print(f"Value: {x}, Threshold: {t1}, Status: {assign_status(x, t1)}")
    print(f"Value: {x}, Threshold: {t2}, Status: {assign_status(x, t2)}")
    print(f"Value: 3, Threshold: 5, Status: {assign_status(3, 5)}")
    print(f"Value: 5, Threshold: 5, Status: {assign_status(5, 5)}")
    print(f"Value: 15, Threshold: 10, Status: {assign_status(15, 10)}")
    print(f"Value: 2, Threshold: 10, Status: {assign_status(2, 10)}")