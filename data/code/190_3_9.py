class FloatMembershipChecker:
    @staticmethod
    def check_value_exists(float_list, target):
        return target in float_list

if __name__ == '__main__':
    sample_floats = [1.5, 2.5, 3.5, 4.5]
    value_to_check = 3.5
    result = FloatMembershipChecker.check_value_exists(sample_floats, value_to_check)
    print(f"Is {value_to_check} in {sample_floats}? {result}")