class DecisionMaker:
    VALID_STATES = {'true', 'false', '1', '0', 'yes', 'no', 'on', 'off'}
    TRUTHY_VALUES = {'true', '1', 'yes', 'on'}

    @staticmethod
    def parse_bool(raw_value):
        if not isinstance(raw_value, (bool, int, float, str)):
            raise ValueError(f"Unsupported type for criteria: {type(raw_value)}")
        
        if isinstance(raw_value, bool):
            return raw_value
        
        if isinstance(raw_value, (int, float)):
            return raw_value != 0
        
        if isinstance(raw_value, str):
            stripped = raw_value.strip().lower()
            if stripped in DecisionMaker.VALID_STATES:
                return stripped in DecisionMaker.TRUTHY_VALUES
            raise ValueError(f"Invalid boolean string representation: '{raw_value}'")
        
        return False

    def evaluate(self, criteria_list):
        if not isinstance(criteria_list, (list, tuple)):
            raise ValueError("Criteria must be a list or tuple.")
        
        if not criteria_list:
            return False
        
        evaluated_results = [self.parse_bool(item) for item in criteria_list]
        
        return any(evaluated_results)

if __name__ == '__main__':
    decision_maker = DecisionMaker()
    criteria_set = [False, "no", 0, "True", "off"]
    result = decision_maker.evaluate(criteria_set)
    print(result)