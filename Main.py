from datetime import datetime

def convertFromFormat1(jsonObject):
    loc = jsonObject["location"].split("/")

    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": {
            "country": loc[0].capitalize(),
            "city": loc[1].capitalize(),
            "area": loc[2],
            "factory": loc[3],
            "section": loc[4],
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }


def convertFromFormat2(jsonObject):
    # convert timestamp to milliseconds
    dt = datetime.fromisoformat(jsonObject["timestamp"].replace("Z", "+00:00"))
    milliseconds = int(dt.timestamp() * 1000)

    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": milliseconds,
        "location": {
            "country": jsonObject["location"]["country"].capitalize(),
            "city": jsonObject["location"]["city"].capitalize(),
            "area": jsonObject["location"]["area"],
            "factory": jsonObject["location"]["factory"],
            "section": jsonObject["location"]["section"]
        },
        "data": {
            "status": jsonObject["data"]["status"],
            "temperature": jsonObject["data"]["temperature"]
        }
    }
