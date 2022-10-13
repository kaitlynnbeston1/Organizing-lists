# creating and printing the list in origenal form.
fav_bands = ["bring me the horizon", "trivium", "metallica", "all that remains", "polyfia"]
print(fav_bands)
# temperarily sorting the list.
print(sorted(fav_bands, reverse=True))
# inserting items
print("I have thought of a couple more, and added them to the list.")
fav_bands.insert(1, "my chemical romance")
fav_bands.append("mayday parade")
fav_bands.insert(3, "black sabbath")
print(fav_bands)
# removing items from list.
stopped_listening = fav_bands.pop()
stopped_listening_ii = "trivium"
fav_bands.remove(stopped_listening_ii)
print(f"{stopped_listening.title()} was removed from the list, as well as {stopped_listening_ii} because I no longer listen to them.") 
print(fav_bands)
# perminantly sorting the list alphabetically.
fav_bands.sort()
print(f"I have a total of {len(fav_bands)} favorite bands, and they are as follows: {fav_bands}.")
