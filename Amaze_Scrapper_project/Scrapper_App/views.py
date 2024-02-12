from django.shortcuts import render
from .models import ScrapedData

def scrape_and_save(request):
    # Your scraping logic here
    # Example: Scrape data from a website and save it to the database
    scraped_data = [{'title': 'Title 1', 'content': 'Content 1', 'url': 'https://example.com/1'},
                    {'title': 'Title 2', 'content': 'Content 2', 'url': 'https://example.com/2'}]
    for data in scraped_data:
        ScrapedData.objects.create(title=data['title'], content=data['content'], url=data['url'])
    return render(request, 'scraped_data.html', {'data': ScrapedData.objects.all()})
