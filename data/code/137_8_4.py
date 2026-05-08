def assign_status(value, threshold):
    return "Greater" if value > threshold else ("Less" if value < threshold else "Equal")
if __name__ == '__main__':
    x = 10
    t1 = 5
    t2 = 10
    status1 = assign_status(x, t1)
    status2 = assign_status(x, t2)
    status3 = assign_status(10, 10)
    status4 = assign_status(3, 5)
    print(f"Value: {x}, Threshold: {t1}, Status: {status1}")
    print(f"Value: {x}, Threshold: {t2}, Status: {status2}")
    print(f"Value: 10, Threshold: 10, Status: {status3}")
    print(f"Value: 3, Threshold: 5, Status: {status4}")