from datetime import date, timedelta

class Student:
    """A student class as basis for method testing"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name  # the underscore shows other developers that it's read-only
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"


    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"


    def alert_santa(self):
        self.naughty_list = True