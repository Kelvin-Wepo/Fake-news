from bs4 import BeautifulSoup

# define a function that takes in a url and returns True if the news is fake and False if it is real
def detect_fake_news(url):
  # use Beautiful Soup to parse the HTML of the page at the given url
  soup = BeautifulSoup(url, 'html.parser')
  
  # find all of the links on the page
  links = soup.find_all('a')
  
  # for each link, check if it is a known source of fake news
  for link in links:
    if link.get('href') in known_fake_news_sources:
      return True
      
  # if none of the links are from known fake news sources, return False
  return False
  
# define a list of known fake news sources
known_fake_news_sources = [
  'fakenews.com',
  'fake-news.net',
  'notarealnewssite.org',
]

# test the detect_fake_news function
print(detect_fake_news('https://ntvkenya.co.ke/news-features/ntv-presents-why-raila-lost/'))  # should return False
print(detect_fake_news('https://ntvkenya.co.ke/news-features/ntv-presents-why-raila-lost/'))  # should return True
