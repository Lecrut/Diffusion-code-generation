def year_difference(year1, year2):
    return year1 - year2
if __name__ == '__main__':
    test_case_1_result = year_difference(2024, 2020)
    print(f"Test Case 1 (2024 - 2020): {test_case_1_result}")
    assert test_case_1_result == 4
    test_case_2_result = year_difference(1990, 2005)
    print(f"Test Case 2 (1990 - 2005): {test_case_2_result}")
    assert test_case_2_result == -15
    test_case_3_result = year_difference(2025, 2025)
    print(f"Test Case 3 (2025 - 2025): {test_case_3_result}")
    assert test_case_3_result == 0
    test_case_4_result = year_difference(1800, 1750)
    print(f"Test Case 4 (1800 - 1750): {test_case_4_result}")
    assert test_case_4_result == 50