from bs4 import BeautifulSoup as bs
count = 1
breaker = 1
with open("film.html") as file:
    src = file.read()

soup = bs(src, "lxml")

title_1 = soup.title
title_2 = soup.find("div", class_="sc-dae4a1bc-0 gwBsXc")

raiting = soup.find("span", class_="sc-7ab21ed2-1 jGRxWM")

year = soup.find("span", class_="sc-8c396aa2-2 itZqyK")

duration = soup.select('ul.ipc-inline-list.ipc-inline-list--show-dividers.sc-8c396aa2-0.kqWovI.baseAlt li[role="presentation"]')[2]
duration_without_spacebar = (duration.text.split())

genre = soup.find("span", class_="ipc-chip__text")

storyline = soup.find("div", class_="ipc-html-content-inner-div")
storyline_without_spacebar = (storyline.text.split())

director = soup.find("a", class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")
director_without_spacebar = (director.text.split())

writers = soup.find_all("a", class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")

actors = soup.find_all("a", class_="sc-bfec09a1-1 gfeYgX")

print(f"{title_2.text.strip()}")
#print(f"Ukrainian title: {title_1.text}") не знаю як перевести в нормальне кодування
print(f"\nYear of data: {year.text}")
print(f"\nDuration of the film: {''.join(duration_without_spacebar)}")
print(f"\nRaiting: {raiting.text}|10")
print(f"\nGenre: {genre.text}")
# print(f"\nStoryline: {' '.join(storyline_without_spacebar)}\n") на сайті опис фільму є не в html а як файл js,
# а ця бібліотека не вміє таке зчитувати, але вона спарсила якись інший текст
print(f"\nDirector: {' '.join(director_without_spacebar)}\n")


for i in writers:
    if breaker < 3:
        writers_without_spacebar = ' '.join(i).split()
        print(f"Writers №{breaker}: {' '.join(writers_without_spacebar)}")
        breaker += 1
    else:
        break

print('\n')

for i in actors:
    print(f"Actor №{count}: {i.text}")
    count += 1