if __name__ == '__main__':
    numerator = 3
    denominator = 4
    target_numerator = 15
    if denominator != 0:
        new_denominator = (target_numerator * denominator) / numerator
        if new_denominator == int(new_denominator):
            final_denominator = int(new_denominator)
        else:
            final_denominator = new_denominator
        print(f"Original Ratio: {numerator}/{denominator}")
        print(f"Target Numerator: {target_numerator}")
        print(f"New Denominator: {final_denominator}")
    else:
        print("Error: Denominator cannot be zero.")