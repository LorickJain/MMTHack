from urllib import request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import datetime


plt.style.use('ggplot')
ticket_prices = []
#ONLY FOR 23rd OCTOBER, UNCOMMENT CODE BELOW FOR THAT DATE.
#url = "https://flights.makemytrip.com/makemytrip/search/R/R/E/1/0/0/S/V0/BLR_DEL_23-10-2016,DEL_BLR_23-10-2016?intid=DF_LP_Widget_Search_Bangalore_New-Delhi"
departure_date = str(input("Enter departure date in the format dd-mm-yyyy"))
arrival_date = str(input("Enter arrival date in the format dd-mm-yyyy"))
departure_city = str(input("Enter departure city(without spaces eg:new-delhi)"))
arrival_city =  str(input("Enter arrival city"))
departure_city = departure_city.lower()
arrival_city = arrival_city.lower()
dep_code = ""
arr_code = ""
print(len(departure_date))
cities = {'agartala': 'IXA', 'agra': 'AGR', "ahmedabad" : "AMD", "allahabad" : "IXD", "amritsar" : "ATQ", "aurangabad" : "IXU", "bagdogra" : "IXB", "bangalore": "BLR", "bhavnagar" : "BHU", "bhopal": "BHO", "bhubaneswar" : "BBI", "bhuj" : "BHJ", "kolkata" : "CCU", "calcutta": "CCU", "chandigarh" : "IXC", "chennai" : "MAA","cochin" : "COK", "coimbatore" : "CJB", "daman" : "NMB","dehradun" : "DED", "dibrugarh" : "DIB", "dimapur" : "DMU", "diu" : "DIU", "gauhati" : "GAU","goa" : "GOI", "gwalior" : "GWL", "hubli" : "HBX", "hyderabad" : "HYD", "imphal" : "IMF", "indore" : "IDR", "jaipur" : "JAI", "jammu" : "IXJ","jamnagar" : "JGA", "jamshedpur" : "IXW", "jodhpur" : "JDH","jorhat" : "JRH","kanpur" : "KNU", "khajuraho" : "HJR", "calicut" : "CCJ", "leh" : "IXL", "lucknow" : "LKO", "ludhiana" : "LUH", "madurai" : "IXM", "mangalore" : "IXE", "bombay" : "BOM","mumbai" : "BOM", "nagpur" : "NAG","nanded" : "NDC", "nasik" : "ISK" ,"new-delhi" : "DEL" ,"patna" : "PAT", "pondicherry" : "PNY", "pune" : "PNQ", "porbandar" : "PBD", "portblair" : "IXZ", "puttaparthi" : "PUT", "raebareli" : "BEK" ,"rajkot" : "RAJ" ,"ranchi" : "IXR", "shillong" : "SHL", "silchar" : "IXS", "srinagar" : "SXR","surat" : "STV", "tezpur" : "TEZ" ,"tiruchirapally" : "TRZ" ,"tirupati" : "TIR", "trivandrum" : "TRV","udaipur" : "UDR", "vadodara" : "BDQ", "varanasi" : "VNS", "vijayawada" : "VGA","vishakhapatnam" : "VTZ"
}
if departure_city or arrival_city in cities:
	dep_code = cities[departure_city]
	arr_code = cities[arrival_city]
else:
    print("Please enter an appropriate city")

if len(departure_date) !=10:
	print("Invalid date, please enter a valid date!")

if len(arrival_date) !=10:
    print("Invalid date, please enter a valid date!")

# url = "https://flights.makemytrip.com/makemytrip/search/R/R/E/1/0/0/S/V0/BLR_DEL_23-10-2016,DEL_BLR_23-10-2016?intid=DF_LP_Widget_Search_Bangalore_New-Delhi"
url = "https://flights.makemytrip.com/makemytrip/search/R/R/E/1/0/0/S/V0/" + dep_code + "_" + arr_code + "_" + departure_date + "," +arr_code + "_" + dep_code+ "_" + arrival_date + "?intid=DF_LP_Widget_Search_"+ departure_city.title() + "_" + arrival_city.title()
connection = request.urlopen(url)
source = connection.read()
soup = BeautifulSoup(source, "html.parser")

for i in soup.find_all('p', {'class': 'splt_orgnl_prce'}):
    print(i.getText())
    print(i.contents)

	#ticket_prices.append(i.title)
#print(ticket_prices)
#actual_price = ticket_prices[0]
#print(actual_price)
print(datetime.datetime.now().strftime('%H:%M:%S'))
 #It will write output in the file , then do cat * > all_prices.txt, means after you run it multiple times and for every half an hour it creates a new file, concatenate all these.



# try using import glob, os, sys to open files and handle them, so after concatenating open them then, read the data in a list or a numpy array and plot
# objects = (time[0], etc...)edit this
# y_pos = np.arange(len(objects))
# actually follow this
# objects = ('total', 'div', 'span', 'anchors')
# values in vertical axis
# y_pos = np.arange(len(objects))
# Return evenly spaced values within a given interval.
# performance = [total, div_count, span_count, anchor]

# plt.bar(y_pos, performance, align='center', alpha=0.5)
# bar graph with performance and y_pos
# plt.xticks(y_pos, objects)
# plt.ylabel('Number of tags')
# name of y axis
# plt.title('Individual tags vs Total tags')
# title of the graph

# plt.show()



