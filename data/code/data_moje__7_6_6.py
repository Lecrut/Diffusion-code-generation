import unittest

def seconds_to_components(total_seconds):
    if not isinstance(total_seconds, (int, float)):
        raise TypeError("Input must be an integer or float")
    if total_seconds < 0:
        raise ValueError("Input must be non-negative")
    
    days = int(total_seconds // 86400)
    remaining = total_seconds % 86400
    hours = int(remaining // 3600)
    remaining = remaining % 3600
    minutes = int(remaining // 60)
    seconds = remaining % 60
    
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

def components_to_seconds(components):
    if not isinstance(components, dict):
        raise TypeError("Input must be a dictionary")
    
    required_keys = ["days", "hours", "minutes", "seconds"]
    for key in required_keys:
        if key not in components:
            raise ValueError(f"Missing key: {key}")
    
    try:
        days = int(components["days"])
        hours = int(components["hours"])
        minutes = int(components["minutes"])
        seconds = int(components["seconds"])
    except (ValueError, TypeError):
        raise ValueError("All time components must be convertible to integers")
    
    if days < 0 or hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components must be non-negative")
    
    return days * 86400 + hours * 3600 + minutes * 60 + seconds

class TestTimeConversion(unittest.TestCase):
    def test_zero_values(self):
        result = seconds_to_components(0)
        self.assertEqual(result["days"], 0)
        self.assertEqual(result["hours"], 0)
        self.assertEqual(result["minutes"], 0)
        self.assertEqual(result["seconds"], 0)
        
        result = components_to_seconds({"days": 0, "hours": 0, "minutes": 0, "seconds": 0})
        self.assertEqual(result, 0)

    def test_small_values(self):
        result = seconds_to_components(61)
        self.assertEqual(result["minutes"], 1)
        self.assertEqual(result["seconds"], 1)
        self.assertEqual(result["days"], 0)
        self.assertEqual(result["hours"], 0)

        result = components_to_seconds({"days": 0, "hours": 0, "minutes": 1, "seconds": 30})
        self.assertEqual(result, 90)

    def test_large_time_spans(self):
        large_seconds = 999999999
        result = seconds_to_components(large_seconds)
        expected_days = 11574
        expected_hours = 1
        expected_minutes = 46
        expected_seconds = 39
        self.assertEqual(result["days"], expected_days)
        self.assertEqual(result["hours"], expected_hours)
        self.assertEqual(result["minutes"], expected_minutes)
        self.assertEqual(result["seconds"], expected_seconds)

        back_to_seconds = components_to_seconds(result)
        self.assertEqual(back_to_seconds, large_seconds)

    def test_invalid_type_seconds(self):
        with self.assertRaises(TypeError):
            seconds_to_components("not a number")

    def test_invalid_type_components(self):
        with self.assertRaises(TypeError):
            components_to_seconds("not a dict")

    def test_negative_input_seconds(self):
        with self.assertRaises(ValueError):
            seconds_to_components(-1)

    def test_missing_key_components(self):
        with self.assertRaises(ValueError):
            components_to_seconds({"days": 1, "hours": 2})

    def test_negative_components(self):
        with self.assertRaises(ValueError):
            components_to_seconds({"days": 1, "hours": -2, "minutes": 0, "seconds": 0})

    def test_edge_case_max_seconds_in_minute(self):
        result = seconds_to_components(3659)
        self.assertEqual(result["hours"], 1)
        self.assertEqual(result["minutes"], 0)
        self.assertEqual(result["seconds"], 59)

    def test_edge_case_max_seconds_in_hour(self):
        result = seconds_to_components(86399)
        self.assertEqual(result["days"], 0)
        self.assertEqual(result["hours"], 23)
        self.assertEqual(result["minutes"], 59)
        self.assertEqual(result["seconds"], 59)

if __name__ == '__main__':
    print(seconds_to_components(0))
    print(seconds_to_components(3661))
    print(seconds_to_components(999999999))
    print(components_to_seconds({"days": 1, "hours": 2, "minutes": 3, "seconds": 4}))
    print(components_to_seconds({"days": 11574, "hours": 1, "minutes": 46, "seconds": 39}))
    unittest.main()