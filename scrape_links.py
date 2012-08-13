#!/usr/bin/env python
import sys
import os

def get_next_target(page):
    """
    Return next html link found on the page.

    Arguments:
    - `page`: page (excerpt) where to search for the next link.
    """

    # defs
    link_lead = '<a href='
    delimiter = '"'

    # find link
    first_link = page.find(link_lead)

    if first_link == -1:
        return None, 0

    open_quote_id = page.find(delimiter, first_link)
    end_quote_id = page.find(delimiter, open_quote_id + 1)
    url = page[open_quote_id + 1: end_quote_id]

    return url, end_quote_id


def print_all_links(page):
    """
    Arguments:
    - `page`:
    """
    while True:
        link, start_position = get_next_target(page)
        if link:
            print link
            page = page[start_position:]
        else:
            break

if __name__ == '__main__':
    print
    page_path = '/Users/rs/pw/python/udacity/cs101/u2/xkcd.html'

    page_file = open(page_path, "r")
    page = page_file.read()
    page_file.close()


    print_all_links(page)


    print "done!"
