class DecisionMaker:
    ALLOWED_ACTIONS = ('approve', 'deny', 'review')

    @staticmethod
    def _validate_criteria(criteria):
        if not isinstance(criteria, dict):
            raise ValueError("Criteria must be a dictionary")
        for key, value in criteria.items():
            if not isinstance(key, str):
                raise ValueError("Criteria keys must be strings")
            if not isinstance(value, bool):
                raise ValueError("Criteria values must be booleans")
        if len(criteria) == 0:
            raise ValueError("Criteria cannot be empty")
        return criteria

    @staticmethod
    def _check_or_condition(criteria):
        return any(criteria.values())

    def evaluate(self, criteria, action):
        validated_criteria = self._validate_criteria(criteria)
        if action not in self.ALLOWED_ACTIONS:
            raise ValueError(f"Action must be one of {self.ALLOWED_ACTIONS}")
        if not self._check_or_condition(validated_criteria):
            return False
        return True

if __name__ == '__main__':
    dm = DecisionMaker()
    result = dm.evaluate({'is_admin': False, 'has_permission': True}, 'approve')
    print(result)