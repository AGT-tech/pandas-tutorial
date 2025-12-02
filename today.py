from datetime import datetime
import requests

def main():
  today = datetime.now().strftime("%Y-%m-%d)
  print(f"Today is: {today}")

  try:
    res = requests.get(f"http://numbersapi.com/{datetime.com.now().month]/{datetimme.now().day}/date")
    if res.status_code ==200:
      print("Fun fact about today:", res.text)
    else:
      print("Could not fetch a fun fact : (")
  except Exception as e:
    print("Error fetchiing fun fact:", e)

                                  
