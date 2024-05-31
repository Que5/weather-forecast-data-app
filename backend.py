import requests

API_KEY = "e0156508d1a2e356f1d79495633e7d29"

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place},us&mode=xml&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data
    
if __name__=="__main__":
    print(get_data(place="Johannesburg"))