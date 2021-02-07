
clean_cols = ['boliga_id', 'address1', 'address2', 'zipcode', 'list_price', 'living_area',
              'lot_area', 'rooms', 'floors', 'construction_date', 'energy_rating',
              'taxes_pr_month', 'bsmnt_area', 'station_dist_km', 'created_date', 'url', 'gmaps']

print_cols = ['boliga_id', 'address1', 'address2', 'zipcode', 'list_price',
              'living_area', 'lot_area', 'rooms', 'floors', 'construction_date', 'energy_rating',
              'taxes_pr_month', 'bsmnt_area', 'station_dist_km', 'created_date', 'market_days', 'url',
              'gmaps']

# zipcodes to exclude from processing
zipcodes = {
    2860: 'Søborg',
    2900: 'Hellerup',
    2730: 'Herlev',
    2740: 'Skovlunde',
    2750: 'Ballerup',
    2760: 'Måløv',
    3500: 'Værløse',
    2600: 'Glostrup',
    2650: 'Hvidovre',
    2800: 'Kongens Lyngby',
    2820: 'Gentofte',
    2870: 'Dyssegård',
    2920: 'Charlottenlund',
    2930: 'Klampenborg',
    2880: 'Bagsværd',
    2630: 'Taastrup',
    2640: 'Hedehusene',
    4000: 'Roskilde',
    2830: 'Virum',
    2840: 'Holte',
    2625: 'Vallensbæk',
    2665: 'Vallensbæk Strand',
    3460: 'Birkerød',
    3520: 'Farum',
    3540: 'Lynge',
    2970: 'Hørsholm',
    3400: 'Hillerød',
    3450: 'Allerød',
    2950: 'Vedbæk',
    2850: 'Nærum',
    2942: 'Skodsborg'
}