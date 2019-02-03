import scrapy


class MovieSpider(scrapy.Spider):
    name = "movies"
    start_urls = [
        'https://takprosto.cc/spisok-horoshih-filmov-kotorye-stoit-posmotret/',
    ]

    def parse(self, response):
        for instruction in response.css('li.instruction'):
            yield {
                'text': instruction.css('strong::text').get(),
            }