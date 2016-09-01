import fresh_tomatoes 
import media 

#we create instances of class Movie where we store information of the movie
toy_story = media.Movie("Toy Story", "In a world where toys are living things who pretend to be lifeless when their owners are present, a group of toys owned by a six-year-old boy, Andy Davis (John Morris), are caught off-guard when Andy's birthday party is moved up a week, as Andy, his single mother (Laurie Metcalf) and infant sister Molly are preparing to move the following week. ",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "Some blue guys",
                     "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
harry_potter1 = media.Movie("Harry Potter and the Sorcerer's Stone", "Harry Potter is an orphan who is about to find outhe is a very well known wizard",
                            "http://3.bp.blogspot.com/-TF8bS9iO95Q/Tdhgtn3MXTI/AAAAAAAAAi4/66xBC_2W1QU/s1600/harry-potter-y-la-piedra-filosofal-poster.jpg",
                            "https://www.youtube.com/watch?v=VyHV0BRtdxo")
finding_nemo = media.Movie("Finding Nemo", "A clown fish is lost and his father goes throuht the see looking form him acompanied by Dory, a fish with a memory problem",
                           "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")
eat_prey_love = media.Movie("Eat Prey Love", "A woman looks for answers about being happy",
                            "http://ia.media-imdb.com/images/M/MV5BMTY5NDkyNzkyM15BMl5BanBnXkFtZTcwNDQyNDk0Mw@@._V1_SX640_SY720_.jpg",
                            "https://www.youtube.com/watch?v=_tlMo1S8HNE")
forrest_gump = media.Movie("Forrest Gump", "A slow witted boy has a life full of events that mark his life and that of others",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=uPIEn0M8su0")

movies = [toy_story, avatar, harry_potter1, finding_nemo, eat_prey_love, forrest_gump]
fresh_tomatoes.open_movies_page(movies)

