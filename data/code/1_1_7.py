class WeightManager:
    def __init__(self):
        self._weights = {}  # Dictionary to store weight measurements
    
    def add_weight(self, user_id: str, weight: float) -> None:
        """Add or update a weight measurement for a specific user."""
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number.")
        self._weights[user_id] = weight
    
    def get_weight(self, user_id: str) -> float | None:
        """Retrieve the latest weight measurement for a user. Returns None if not found."""
        return self._weights.get(user_id)
    
    def update_weight(self, user_id: str, new_weight: float) -> bool:
        """Update an existing weight measurement or raise KeyError if user doesn't exist."""
        if user_id in self._weights:
            self._weights[user_id] = new_weight
            return True
        else:
            # If the key does not exist but we still want to update, treat it as add (optional behavior)
            # Based on strict interpretation of "update", returning False is safer for existing logic.
            raise KeyError(f"User '{user_id}' has no weight record.")

    def remove_weight(self, user_id: str) -> bool:
        """Remove a weight measurement if it exists."""
        return self._weights.pop(user_id, None) is not None
    
    def get_all_weights(self) -> dict[str, float]:
        """Return a copy of all stored weights to prevent external modification."""
        return dict(self._weights)

if __name__ == '__main__':
    # Hard-coded sample values for testing the WeightManager class
    manager = WeightManager()

    # Add initial data
    manager.add_weight("alice", 65.0)
    manager.add_weight("bob", 72.5)
    
    print(f"Alice's weight: {manager.get_weight('alice')}")  # Output: Alice's weight: 65.0

    # Update Bob's weight
    try:
        result = manager.update_weight("bob", 74.0)
        if result:
            print(f"Bob's updated weight: {manager.get_weight('bob')}")  # Output: Bob's updated weight: 74.0
        
        # Attempt to update non-existent user (should raise error based on strict 'update' logic defined in class)
    except KeyError as e:
        print(e)

    # Try updating a new entry using the method that raises for missing keys, 
    # then demonstrate removal and retrieval of all.
    
    try:
        manager.update_weight("charlie", 50.0)
    except KeyError as e:
        pass
    
    # Remove Alice's record
    removed = manager.remove_weight("alice")
    print(f"Alice removed? {removed}")

    # Get remaining data
    all_data = manager.get_all_weights()
    print(f"Remaining users and weights: {all_data}")