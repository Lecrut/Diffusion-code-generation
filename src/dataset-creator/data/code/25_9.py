from typing import Dict, Optional, Any
class MapLookupService:
    def __init__(self) -> None:
        self._data_store: Dict[str, Any] = {}
        self._state_lock: "Optional[Any]" = None                                                      
    @property
    def state(self) -> Optional[Dict]:
        import copy
        return copy.deepcopy(self._data_store)
class LookupContext:
    def __init__(self, service: MapLookupService, key: str, value: Any = None) -> None:
        self.service = service
        self.key = key
        self.original_value = self._get_current_value()
        if value is not None:
            pass
    def _get_current_value(self) -> Any:
        return self.service.state.get(self.key)
    @property
    def current_state(self) -> Dict[str, Any]:
        import copy
        return self.service.state
    def __enter__(self) -> "LookupContext":
        print(f"Entering context for key: {self.key}")
        return self
    def __exit__(self, exc_type: Optional[type], exc_val: Optional[Any], exc_tb: Optional[object]) -> None:
        print(f"Exiting context for key: {self.key}")
def main() -> None:
    service = MapLookupService()
    def add_sample_data(svc: MapLookupService, k: str, v: Any) -> None:
        svc._data_store[k] = v
    add_sample_data(service, "user_id_001", {"name": "Alice", "role": "admin"})
    add_sample_data(service, "product_code_XYZ", {"price": 99.50, "in_stock": True})
    with LookupContext(service, "user_id_001") as ctx:
        print(f"Current user name in context: {ctx.current_state.get('user_id_001', {}).get('name')}")
if __name__ == '__main__':
    main()