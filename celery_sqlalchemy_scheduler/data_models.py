from pydantic import BaseModel, validator


class Schedule(BaseModel):
    minute: str = "*"
    hour: str = "*"
    day_of_week: str = "*"
    day_of_month: str = "*"
    month_of_year: str = "*"

    @validator("minute")
    def minute_validation(cls, v):
        if "*" == v:
            return v
        elif not v.isdigit():
            raise ValueError(f"{v} is not a valid int")
        assert int(v) >= 0 and int(v) < 60, "Minute value must range between 0 and 59"
        return v

    @validator("hour")
    def hour_validation(cls, v):
        if "*" == v:
            return v
        elif not v.isdigit():
            raise ValueError(f"{v} is not a valid int")
        assert int(v) >= 0 and int(v) < 24, "Hour value must range between 0 and 23"
        return v

    @validator("day_of_week")
    def day_of_week_validation(cls, v):
        if "*" == v:
            return v
        elif not v.isdigit():
            raise ValueError(f"{v} is not a valid int")
        assert int(v) >= 0 and int(v) < 7, "Day of the week value must range between 0 and 6"
        return v

    @validator("day_of_month")
    def day_of_month_validation(cls, v):
        if "*" == v:
            return v
        elif not v.isdigit():
            raise ValueError(f"{v} is not a valid int")
        assert int(v) > 0 and int(v) < 32, "Day of the month value must range between 1 and 31"
        return v

    @validator("month_of_year")
    def month_of_year_validation(cls, v):
        if "*" == v:
            return v
        elif not v.isdigit():
            raise ValueError(f"{v} is not a valid int")
        assert int(v) > 0 and int(v) < 13, "Mon value must range between 0 and 59"
        return v


class ScheduledTask(BaseModel):
    name: str
    task: str
    schedule: Schedule
