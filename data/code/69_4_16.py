from decimal import Decimal, getcontext

getcontext().prec = 50

def miles_to_feet(miles):
    feet_per_mile = Decimal("5280")
    miles_decimal = Decimal(str(miles))
    return miles_decimal * feet_per_mile

if __name__ == "__main__":
    sample_miles = "1.5"
    result = miles_to_feet(sample_miles)
    print(result)