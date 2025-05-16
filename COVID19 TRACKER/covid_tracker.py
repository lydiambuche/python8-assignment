import pandas as pd
import matplotlib.pyplot as plt

# Function to download and load the data
def load_data(url):
    covid_data = pd.read_csv(url)
    return covid_data

# Function to clean and process the data
def clean_data(covid_data):
    covid_data_melted = covid_data.melt(id_vars=["Province/State", "Country/Region", "Lat", "Long"], 
                                        var_name="Date", value_name="Confirmed")
    covid_data_melted["Date"] = pd.to_datetime(covid_data_melted["Date"])
    return covid_data_melted

# Function to generate the trend visualization
def plot_trends(covid_data_melted, country_name):
    covid_country = covid_data_melted[covid_data_melted["Country/Region"] == country_name]
    plt.figure(figsize=(10,6))
    plt.plot(covid_country["Date"], covid_country["Confirmed"], label="Confirmed Cases")
    plt.title(f"COVID-19 Confirmed Cases in {country_name}")
    plt.xlabel("Date")
    plt.ylabel("Confirmed Cases")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Main function to run the script
def main():
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    covid_data = load_data(url)
    covid_data_melted = clean_data(covid_data)
    plot_trends(covid_data_melted, "US")  # Plot trends for the US
    
if __name__ == "__main__":
    main()
    
